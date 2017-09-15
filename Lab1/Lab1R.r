#Sameena Bajwa
#CS237
#Lab 1 R Code

#commands that were typed directly into the console

#Problem 7, loading and viewing the csv file
data <- read.csv (file = "grades.csv", head = TRUE, sep = ",")
data 

#Problem 8 - summary of the data
summary (data)

#Problem 9 - standard deviation for each class
sd(data$class1)
sd(data$class2)
sd(data$class3)

#Problem 10 - creating side by side boxplots
boxplot (data)

#Problem 11 - plotting the PMF for each class
mytable <- table(data$class1)
mytable <- (mytable / sum(mytable))
plot(mytable)

mytable <- table(data$class2)
mytable <- (mytable / sum(mytable))
plot(mytable)

mytable <- table(data$class3)
mytable <- (mytable / sum(mytable))
plot(mytable)

