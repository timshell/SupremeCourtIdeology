data <- read.table("data.txt", header = T)

miles <- as.vector(data$Miles)

feelings <- as.vector(data$Feeling)

good <- feelings == "Good"
bad <- feelings == "Bad"
meh <- feelings == "Meh"

good[good == FALSE] <- NA
bad[bad == FALSE] <- NA
meh[meh == FALSE] <- NA


plot(miles, xlab="", ylab="Miles", type="n", main="Mileage in College", xaxt='n', 
     yaxs="i", ylim = range(0:85))
lines(miles)
points(miles[bad], pch = 21, col="red", bg="red")
points(miles[good], pch = 21, col="green", bg="green")
points(miles[meh], pch = 21, col="yellow", bg="yellow")
