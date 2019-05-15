library(aod)
library(ggplot2)
library(glmnet)
library(caret)
library(mlbench)
library(glmnet)
library(randomForest)
library(hdi)
library(neuralnet)

data<- read.csv("multi-cohortd.csv",header = TRUE)
str(data, list.len=ncol(data))

##XG requires numeric labels
XGlabel <- data$label

##convert bools to factors
##male: 0; female: 1
data$gender<-as.factor(data$gender)
data$label<-as.factor(data$label)
data$obese<-as.factor(data$obese)

##prepare the matrix from data frame for glm
x<-model.matrix(label~.,data=data)

##throw away near Zero Variances
x<-x[,-nearZeroVar(x)]
x=x[,-1]

##elastic net with 5 fold cross validation
glmnet1<-cv.glmnet(x=x,y=data$label,type.measure='class',nfolds=5,alpha=.5,family="binomial")

##get non zero coefficients at lambda.min
c<-coef(glmnet1,s='lambda.min',exact=TRUE)
inds<-which(c!=0)
variables<-row.names(c)[inds]
variables

##pick the elastic net features
reducedFeatures <- data[,which(names(data) %in% variables)]
reducedFeatures$label <- data$label
reducedFeaturesXG<-model.matrix(label~.,data=reducedFeatures)

##pvalues using hdi
outlasso <- lasso.proj(x,y,family="binomial") 

##Boosted trees
bstDense <- xgboost(reducedFeaturesXG, XGlabel, max.depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic")

##Split 
smp_size <- floor(0.75 * nrow(reducedFeatures))

## set the seed to make your partition reproductible
set.seed(123)
data_ind <- sample(seq_len(nrow(reducedFeatures)), size = smp_size)

train2 <- reducedFeatures[data_ind, ]
test2 <- reducedFeatures[-data_ind, ]

##Well, this should not be done (prefect seperation) 
model <- glm(label ~.,family=binomial(link='logit'),data=train2,control = list(maxit = 100))

model <- randomForest(label ~ ., data = train2, importance = TRUE)

summary(model)
library(caret)
varImp(model)

##
modelFit <- train(label~.,data=data, method="rf" ,importance = TRUE)
varImp(modelFit)
coeff<-model$coefficients

# NN
scaleddata<-scale(data)


## Model, please modify the hidden layers config according to accuracy 
nn <- neuralnet(label ~ ., data=train2, hidden=c(2,1), linear.output=FALSE, threshold=0.01)
##result matrix
nn$result.matrix
## plot of nwtworks 
plot(nn)
# matrix 
nn$result.matrix

## testing
#Test the resulting output
temp_test <- subset(test2, select = -c(label))
#temp_test <- subset(testset, select = c("fcfps","earnings_growth", "de", "mcap", "current_ratio"))
head(temp_test)
nn.results <- compute(nn, temp_test)
results <- data.frame(actual = test2$label, prediction = nn.results$net.result)
rresults<-results
##
rresults[,-1] <-round(results[,-1],0) #the "-1" excludes column 1
rresults
## rounding 
roundedresultsdf=data.frame(rresults)

##
table(actual,roundedresultsdf$prediction.1)


## convert coeff matric into data frame 
df <- as.data.frame(as.matrix(c))
write.csv(df,'lasso.csv')

## Remove all zero rows from df
df1<-as.data.frame(df[df$coff != 0, ])
df$1<-as.numeric(df$1)

###stepwise takes forever to complete, use hdi package to compute the pvalues instead

fullmod = glm(label ~., family=binomial(link='logit'),data=data,control = list(maxit = 100))
summary(fullmod)

#Null model
nothing <- glm(label ~ 1,family=binomial(link='logit'),data=data,control = list(maxit = 100))

##
backwards = step(fullmod)
