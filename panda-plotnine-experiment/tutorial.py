import pandas as pd
from plotnine import *

# following tutorial
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

top_wines = reviews[reviews['variety'].isin(reviews['variety'].value_counts().head(5).index)]

df = top_wines.head(1000).dropna()

# simple scatter graph
p = (ggplot(df)
 + aes('points', 'price')
 + geom_point())

print(p)

# fancy graph
g=(ggplot(top_wines)
     + aes('points', 'variety')
     + geom_bin2d(bins=20)
)

print(g)

# Mcdonalds dataset
# Is there a type of food way more higher in calories than others? Do salads tend to have higher calories than others?
mcd = pd.read_csv("menu.csv", index_col=0)
items = mcd[mcd['Category'].isin(mcd['Category'].value_counts().index)]

plot = (ggplot(items)
 + aes('Calories', 'Category')
 + geom_bin2d(bins=20)
 + ggtitle("McDonald food Categories and their Calorie Distribution")
+ theme_xkcd()
        )
print(plot)


plot = (ggplot(items)
 + aes('Calories from Fat', 'Category')
 + geom_bin2d(bins=5)
 + ggtitle("McDonald food Categories and their Calories from Fat")
)
print(plot)

# visualize restaurant inspection scores
r = pd.read_csv("restaurant.csv", index_col=0)
plot = (ggplot(r)
  + aes('risk_category')
+ geom_bar(stat="bin")
+scale_color_grey() + theme_classic()
 + ggtitle("Risk level of Restaurants in San Francisco")
)
print(plot)