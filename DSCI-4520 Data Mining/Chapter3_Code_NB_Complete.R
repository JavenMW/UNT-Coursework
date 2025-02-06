## Naive Bayes classifier
## in this practice we use Student Retention data to build
## a Naive Bayes classifier by the naive Bayes function from the e1071 package

## First we create a Naive Bayes classifier to predict a single record
## Then, we calculate the confusion matrix and performance metrics for the model
list.of.packages <- c("ggplot2", "e1071", "caret", "pROC", "MASS", "dplyr")
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
# XXX is the name of the variable that you found in the previous step
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


###################################################
# build a naive Bayes classifier
# replace XXX with the name of the function that create a Naive Bayes classifier
# The function is in the e1071 library
ret.nb.model <- naiveBayes(Fall_Retention ~ ., data = train.df)
# see the model results
ret.nb.model



# calculate the confusion matrix for the classifier
# training
train.pred.class <- predict(ret.nb.model, newdata = train.df)
#replace XXX with the name of the function that calculates the confusion matrix
confusionMatrix(train.pred.class, train.df$Fall_Retention)

# validation
valid.pred.class <- predict(ret.nb.model, newdata = valid.df)
#replace XXX with the name of the function that calculates the confusion matrix
confusionMatrix(valid.pred.class, valid.df$Fall_Retention)

# Create ROC curve for training set
train.pred.p <- predict(ret.nb.model, newdata = train.df,type = "raw")
# Replace XXX with the name of the function that create ROC plot
# The function is from the pROC library
roc(train.df$Fall_Retention,as.vector(train.pred.p[,1]),
    percent=F, ci.alpha=.9, stratified=FALSE, plot=TRUE, grid=TRUE,
    show.thres=TRUE, legacy.axes = TRUE,reuse.auc = TRUE,asp=0,
    # print.thres = c(0.30,0.35, 0.40, 0.45,0.48, 0.50,0.55, 0.60),#
    print.auc = TRUE, print.thres.col = "blue" )


# Create ROC curve for validation set
valid.pred.p <- predict(ret.nb.model, newdata = valid.df,type = "raw")
# Replace XXX with the name of the function that create ROC plot
# The function is from the pROC library
roc(valid.df$Fall_Retention,as.vector(valid.pred.p[,1]),
    percent=F, ci.alpha=.9, stratified=FALSE, plot=TRUE, grid=TRUE,
    show.thres=TRUE, legacy.axes = TRUE,reuse.auc = TRUE,asp=0,
    # print.thres = c(0.30,0.35, 0.40, 0.45,0.48, 0.50,0.55, 0.60),#
    print.auc = TRUE, print.thres.col = "blue" )
