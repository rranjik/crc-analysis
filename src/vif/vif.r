library(aod)
library(ggplot2)
library(glmnet)
library(caret)
library(mlbench)

data<- read.csv("multi-cohortd.csv",header = TRUE)
str(data, list.len=ncol(data))

data$gender<-as.factor(data$gender)
data$label<-as.factor(data$label)
data$obese<-as.factor(data$obese)

## 
library(glmnet)

x<-model.matrix(label~.,data=data)
x<-x[,-nearZeroVar(x)]
x=x[,-1]

glmnet1<-cv.glmnet(x=x,y=data$label,type.measure='class',nfolds=5,alpha=.5,family="binomial")

c<-coef(glmnet1,s='lambda.min',exact=TRUE)
inds<-which(c!=0)
variables<-row.names(c)[inds]
variables

reducedFeatures <- data[,which(names(data) %in% variables)]

reducedFeatures$label <- data$label

reducedFeaturesXG<-model.matrix(label~.,data=reducedFeatures)

bstDense <- xgboost(reducedFeaturesXG, XGlabel, max.depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic")

resoponse = c(
"Otu1109",
"Otu0967", 
"Otu0817",
"Otu1717",
"Otu1915",
"Otu0745",
"Otu0552",
"Otu0781",
"Otu1985",
"Otu0772",
"Otu0030",

"Otu0302",
"Otu0309",
"Otu0314",
"Otu0915",
"Otu0918",
"Otu1887"
);
##Split 
smp_size <- floor(0.75 * nrow(reducedFeatures))

## set the seed to make your partition reproductible
set.seed(123)
data_ind <- sample(seq_len(nrow(reducedFeatures)), size = smp_size)

train2 <- reducedFeatures[data_ind, ]
test2 <- reducedFeatures[-data_ind, ]

## GLM 

#model <- glm(label ~.,family=binomial(link='logit'),data=train2,control = list(maxit = 100))

library(randomForest)

model <- randomForest(label ~ ., data = train2, importance = TRUE)

summary(model)
library(caret)
varImp(model)

##
modelFit <- train(label~.,data=data, method="rf" ,importance = TRUE)
varImp(modelFit)


coeff<-model$coefficients

## convert coeff matric into data frame 
df <- as.data.frame(as.matrix(c))
write.csv(df,'lasso.csv')
## Remove all zero rows from df
df1<-as.data.frame(df[df$coff != 0, ])
df$1<-as.numeric(df$1)

###stepwise 

fullmod = glm(label ~., family=binomial(link='logit'),data=data,control = list(maxit = 100))
summary(fullmod)

#Null model
nothing <- glm(label ~ 1,family=binomial(link='logit'),data=data,control = list(maxit = 100))

##
backwards = step(fullmod)
