#Sameena Bajwa
#CS237
#Lab5

significance <- function(n, dev, mean, xbar, alternative) {
  zvalue <- (xbar - mean) / (dev / sqrt(n))
  pvalue <- 0

  # additions for problem 15
  if (alternative == "less") {
    pvalue <- pnorm(zvalue)
  } else if (alternative == "two-sided") {
    pvalue <- (2 * (1 - pnorm(zvalue)))
  } else {
    pvalue <- (1 - pnorm(zvalue))
  }
 
  result <- ""
  # print (zvalue)
  # print (pvalue)

  # additions for problem 11
  if (pvalue > .05) {
    result <- "yes"
  
  } else {
    result <- "no"
  
  } 
 cat("sample size: ", n)
 cat("\nsample mean: ", xbar)
 cat("\nz value: ", zvalue)
 cat("\np-value: ", pvalue)

 # return (c(zvalue, pvalue, result))
}

    
# testing problem 10
# significance(4, 100, 500, 550)

# testing problem 11
# answer <- c()
# for (i in (4:11))
#   
#   answer = append(answer, (significance (i, 100, 500, 550)))
# 
# data <- matrix(c(data = answer), ncol = 3, byrow = TRUE)
# colnames(data) <- c("z statistic", "p-value", "significant (yes/no)")
# rownames(data) <- c(4:11)
# data <- as.table(data)
# print (data)


# testing problem 16 - read in the csv file and gather data from desired column
epaData <- read.csv (file = "epa.csv", head = TRUE, sep = ",")
mpg <- epaData$COMB.MPG
samplemean = mean(mpg)
samplesize = length(mpg)

significance(samplesize, 4.7, 20, samplemean, "greater")

# #testing problem 19
# x <- seq(-4, 4, length = 100) * 4.7 + samplemean
# density <- dnorm (x, mean = samplemean, sd = 4.7)
# plot(x, density, type = 'l')
# abline(v = 19.462)
# abline(v = 21.297)

#testing problem 25
# x <- seq(-4, 4, length = 100) 
# density <- dnorm(x)
# plot(x, density, type = 'l')
# lines(x, dt(x,1), col = "yellow")
# lines(x, dt(x,3), col = "blue")
# lines(x, dt(x,8), col = "red")
# lines(x, dt(x,30), col = "darkgreen")
# legend("topright", c("normal", "df = 1", "df = 3", "df = 8", "df = 30"),
#        lty = c(1, 1, 1, 1, 1), col = c("black", "yellow", "blue", "red", "darkgreen"))

#testing problem 30
xbar <- 550
hnull <- 500
sdeviation <- 100
n <- 4
tvalue <- (xbar - hnull) / (sdeviation / sqrt(n))
pvalue <- pt(tvalue, df = n-1, lower.tail = FALSE)
print (pvalue)

#testing problem 33
print(qt(.05, 3))
print(qt(.05, 3, lower.tail = FALSE))




