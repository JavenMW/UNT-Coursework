## Classification and Regression Trees
## in this practice we use Student Retention data to build
## a decision tree classifier to predict student retention

## Load the necessary packages
list.of.packages <- c("ggplot2", "e1071", "caret", "pROC", "MASS", "dplyr", "rpart.plot", "rpart")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

# load all required packages at once
sapply(list.of.packages, require, character.only = TRUE)

# Set the working directory and read the CSV file by replacing XXX
setwd('D:/UNT/Teaching/Fall 2022/DSCI 4520/Term Project')
retention.df <- read.csv('DSCI4520_Project_Data.csv', stringsAsFactors=TRUE, header=T, na.strings='')


# Count the number of unique values (levels) in each column
# search for a variable that has levels with less than 10 counts
table (retention.df$SAP_Group)

# remove the data records with values < 10 in count
retention.df <- retention.df %>%
    filter(!(Acad_Stand_Group %in% c("Missing", "Dismissed")))

retention.df <- retention.df %>%
    filter(!(SAP_Group %in% c("Academic Plan Approved - Financial Aid Eligible", "Zero Hours Completed - Not Eligible for Aid")))


# define two new categorical variables based on the spring and fall retention columns
retention.df$Spring_Retention <- ifelse(retention.df$Spring_Not_Retained == "1", "Spring Not Retained" , "Spring Retained")
retention.df$Fall_Retention <- ifelse(retention.df$Fall_Not_Retained == "1", "Dropped out" , "Retained")

# convert the newly defined variables to factors
retention.df$Fall_Retention <- factor(retention.df$Fall_Retention)
retention.df$Spring_Retention <- factor(retention.df$Spring_Retention)
retention.df$AY <- factor(retention.df$AY)

# drop original Fall_Not_Retained, Spring_Not_Retained, ID, App_Year
retention.df <- retention.df[,!names(retention.df) %in% c("ID", "App_Year", "Spring_Not_Retained", "Fall_Not_Retained")]



# Create training and validation sets.
selected.var <- c(1:21)
train.index <- sample(c(1:dim(retention.df)[1]), dim(retention.df)[1]*0.7)
train.df <- retention.df[train.index, selected.var]
valid.df <- retention.df[-train.index, selected.var]

# create a tree with full complexity: over-fitted
# cp = 0 allows the rpart function to grow a tree to the full complexity level
# notice that we use ALL data to develop a tree to the full complixity level
cp_value <- 0
retention.cart <- rpart(Fall_Retention ~ ., data = train.df, method = "class", cp = cp_value, minsplit = 1)
# count number of leaves
length(retention.cart$frame$var[retention.cart$frame$var == "<leaf>"])
# plot tree
prp(retention.cart, type = 2, tweak=2, extra = 1, under = TRUE, split.font = 1, varlen = -10,
    box.col=ifelse(retention.cart$frame$var == "<leaf>", 'gray', 'white'))

# Calculate confusion matrix for the training and validation sets
# set argument type = "class" in predict() to generate predicted class membership.
retention.cart.pred.train <- predict(retention.cart,train.df,type = "class")
# generate confusion matrix for training data
confusionMatrix(retention.cart.pred.train, as.factor(train.df$Fall_Retention))
# set argument type = "class" in predict() to generate predicted class membership.
retention.cart.pred.val <- predict(retention.cart,valid.df,type = "class")
# generate confusion matrix for training data
confusionMatrix(retention.cart.pred.val, as.factor(valid.df$Fall_Retention))



# At this point, you need to select the optimum value for cp
# First, print out the cross-validation results
printcp(retention.cart)
# Then find the cp value that corresponds to the lowest xerror value
# and create a new tree with the optimum cp value
bestcp <- retention.cart$cptable[which.min(retention.cart$cptable[,"xerror"]),"CP"]
bestcp
cp_value <- bestcp

# This time we use the training set only to grow a tree with the best cp
opt.retention.cart <- rpart(Fall_Retention ~ ., data = train.df, method = "class", cp = cp_value, minsplit = 1)
# plot tree
prp(opt.retention.cart, type = 1, tweak=2, extra = 1, under = TRUE, split.font = 1, varlen = -10,
    box.col=ifelse(opt.retention.cart$frame$var == "<leaf>", 'gray', 'white'))

# Calculate confusion matrix for the training and validation sets
# set argument type = "class" in predict() to generate predicted class membership.
opt.retention.cart.pred.train <- predict(opt.retention.cart,train.df,type = "class")
# generate confusion matrix for training data
confusionMatrix(opt.retention.cart.pred.train, as.factor(train.df$Fall_Retention))
# set argument type = "class" in predict() to generate predicted class membership.
opt.retention.cart.pred.val <- predict(opt.retention.cart,valid.df,type = "class")
# generate confusion matrix for training data
confusionMatrix(opt.retention.cart.pred.val, as.factor(valid.df$Fall_Retention))


# Create ROC curve for training set
train.pred.p <- predict(opt.retention.cart, train.df,type = "prob")
# Replace XXX with the name of the function that create ROC plot
# The function is from the pROC library
roc(train.df$Fall_Retention,as.vector(train.pred.p[,1]),
    percent=F, ci.alpha=.9, stratified=FALSE, plot=TRUE, grid=TRUE,
    show.thres=TRUE, legacy.axes = TRUE,reuse.auc = TRUE,asp=0,
    # print.thres = c(0.30,0.35, 0.40, 0.45,0.48, 0.50,0.55, 0.60),#
    print.auc = TRUE, print.thres.col = "blue" )


# Create ROC curve for validation set
valid.pred.p <- predict(opt.retention.cart, newdata = valid.df,type = "prob")
# Replace XXX with the name of the function that create ROC plot
# The function is from the pROC library
roc(valid.df$Fall_Retention,as.vector(valid.pred.p[,1]),
    percent=F, ci.alpha=.9, stratified=FALSE, plot=TRUE, grid=TRUE,
    show.thres=TRUE, legacy.axes = TRUE,reuse.auc = TRUE,asp=0,
    # print.thres = c(0.30,0.35, 0.40, 0.45,0.48, 0.50,0.55, 0.60),#
    print.auc = TRUE, print.thres.col = "blue" )
