# Install and load the janitor and ggplot2 packages
install.packages("janitor")
install.packages("stargazer")

install.packages("ggplot2")
library(janitor)
library(ggplot2)


# Replace it with the path of your actual dataframe
df <- read.csv("C:\\Users\\PC2\\Downloads\\Crime_Data_from_2020_to_Present_20231021.csv")



# Load necessary libraries
library(janitor)

# Clean column names
df <- clean_names(df)

# Remove rows with NAs
df <- remove_empty(df, "rows")

# View the structure of the dataframe after handling NAs
glimpse(df)

# Display the five-number summary of 'Vict Age' after handling NAs
summary(df$vict_age)



# Load necessary libraries
library(ggplot2)
library(dplyr)
library(lubridate)  # for date manipulation

# Convert DATE OCC to proper date format
df$date_occ <- mdy_hms(df$date_occ)


# Taking a sample of 100 rows from the dataframe
sample_df <- df[sample(nrow(df), 100, replace = FALSE), ]

# Plotting the sample distribution of Vict_Age across DATE_OCC
ggplot(sample_df, aes(x = date_occ, y = vict_age)) +
  geom_point(color = "blue") +
  labs(title = "Sample Distribution of Victim Age Over Time",
       x = "Date of Occurrence",
       y = "Victim Age",
       caption = "Data Source: Sample Dataset") +
  theme_minimal()
ggplot(sample_df, aes(x = date_occ, y = vict_age)) +
  geom_line(color = "red") +
  labs(title = "Sample Line Plot of Victim Age Over Time",
       x = "Date of Occurrence",
       y = "Victim Age",
       caption = "Data Source: Sample Dataset") +
  theme_minimal()

# Running the regression
reg_model <- lm(crm_cd_1 ~ vict_age, data = df)

# Showing the output using summary()
summary(reg_model)
reg_formula_multivariate <- lm(crm_cd_1~ vict_age + vict_sex, data = df)
summary(reg_formula_multivariate)
# Load the necessary library
library(stargazer)



# Create a table to display both regression models
stargazer(reg_model, reg_formula_multivariate, 
          type = "text", 
          title = "Regression Results", 
          align = TRUE, 
          dep.var.labels = c("Dependent Variable"),
          covariate.labels = c("victim age", "victime sex"))
# Running fixed-effects regression controlling for region
fixed_effects_model <- lm(crm_cd_1 ~ vict_age + vict_sex + as.factor(area), data = df)
summary(fixed_effects_model)
# Load the necessary library



# Create an updated table including all models
stargazer(reg_model, reg_formula_multivariate, fixed_effects_model, 
          type = "text", 
          title = "Regression Results Comparison", 
          align = TRUE, 
          dep.var.labels = c("Dependent Variable"),
          covariate.labels = c("victim age", "victim sex"))

