library(randomForest)
data <- read.csv("C:\\Users\\RAGAVENDRA KUMAR R\\OneDrive\\Documents\\CSCI-GA.2565-001 - Machine Learning\\crc-analysis\\data\\multi-cohortd.csv", header = TRUE)
set.seed(100)
train <- sample(nrow(data1), 0.7*nrow(data1), replace = FALSE)
TrainSet <- data[train,]
ValidSet <- data[-train,]
model <- randomForest(label ~ ., data = TrainSet, importance = TRUE)
varImpPlot(model)