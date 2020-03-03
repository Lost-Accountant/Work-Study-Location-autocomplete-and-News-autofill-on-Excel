data <- readxl::read_excel('Self-Immolation and Attack agents.xlsx', 
                           sheet = 'Side by Side Diagram')
data <- data[-nrow(data),]

library(tidyverse)

par(mfrow = c(1,2))

plot1 <- data %>%
  ggplot(aes(x = Year, y = `Attack on Agent`, group = 1)) +
  geom_point() +
  geom_line(color = 'red') +
  theme(text = element_text(size = 18))

plot2 <- data %>%
  ggplot(aes(x = Year, y = `Self Immolation`, group = 1)) +
  geom_point() +
  geom_line(color = 'blue') +
  theme(text = element_text(size = 18))

cowplot::plot_grid(plot1, plot2, labels = 'AUTO')
