## Logistic Regression classifier
## in this practice we use in this practice we use Student Retention data to build
## a logistic regression classifier

## Load the necessary packages
list.of.packages <- c("ggplot2", "e1071", "caret", "pROC", "MASS", "dplyr")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

# load all required packages at once
sapply(list.of.packages, require, character.only = TRUE)

setwd('D:/UNT/Teaching/Fall 2022/DSCI 4520/Term Project')
retention.df <- read.csv("DSCI4520_Project_Data.csv", stringsAsFactors=TRUE, header=T, na.strings='')

# Count the number of unique values (levels) in each column
# search for a variable that has levels with less than 10 counts
table (retention.df$SAP_Group)

# remove the data records with values < 10 in count
retention.df <- retention.df %>%
    filter(!(Acad_Stand_Group %in% c("Missing", "Dismissed")))

retention.df <- retention.df %>%
    filter(!(SAP_Group %in% c("Academic Plan Approved - Financial Aid Eligible", "Zero Hours Completed - Not Eligible for Aid")))

# convert AY to factor
retention.df$AY <- factor(retention.df$AY)

# drop original Fall_Not_Retained, Spring_Not_Retained, ID, App_Year
retention.df <- retention.df[,!names(retention.df) %in% c("ID", "App_Year")]



# Create training and validation sets.
selected.var <- c(1:21)
train.index <- sample(c(1:dim(retention.df)[1]), dim(retention.df)[1]*0.7)
train.df <- retention.df[train.index, selected.var]
valid.df <- retention.df[-train.index, selected.var]


###########################################
# logistic regression model
# fit a model with all variables
ret.logit.model.all <- glm(Fall_Not_Retained ~ ., data = train.df, family = "binomial")
options(scipen=999)
summary(ret.logit.model.all)


# Find a model with a stepwise approach
ret.logit.model.step <- glm(Fall_Not_Retained ~., data = train.df, family = binomial) %>%
    stepAIC(trace = FALSE)
# Summarize the final selected model
summary(ret.logit.model.step)

# Use the model with all variables for prediction
logit.val.pred <- predict(ret.logit.model.all, valid.df, type = "response")
logit.train.pred <- predict(ret.logit.model.all, train.df, type = "response")

#use caret and compute a confusion matrix on the training set
confusionMatrix(data = as.factor(as.numeric(logit.train.pred>0.2)),
                reference = as.factor(train.df$Fall_Not_Retained),positive = "1")

#use caret and compute a confusion matrix on the validation set
confusionMatrix(data = as.factor(as.numeric(logit.val.pred>0.2)),
                reference = as.factor(valid.df$Fall_Not_Retained),positive = "1")


# plot ROC curve - training set
roc(train.df$Fall_Not_Retained, logit.train.pred,
    percent=F, ci.alpha=0.9, stratified=FALSE, plot=TRUE, grid=TRUE,
    show.thres=TRUE, legacy.axes = TRUE,reuse.auc = TRUE,asp=0,
    # print.thres = c(0.30,0.35, 0.40, 0.45,0.48, 0.50,0.55, 0.60),#
    print.auc = TRUE, print.thres.col = "blue" )


# plot ROC curve - validation set
roc(valid.df$Fall_Not_Retained, logit.val.pred,
    percent=F, ci.alpha=0.9, stratified=FALSE, plot=TRUE, grid=TRUE,
    show.thres=TRUE, legacy.axes = TRUE,reuse.auc = TRUE,asp=0,
    # print.thres = c(0.30,0.35, 0.40, 0.45,0.48, 0.50,0.55, 0.60),#
    print.auc = TRUE, print.thres.col = "blue" )
