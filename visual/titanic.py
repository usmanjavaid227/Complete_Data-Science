import seaborn as sns
import matplotlib.pyplot as plt
# set set_theme
sns.set_theme(style="ticks", color_codes=True)

#load dataSet
titanic=sns.load_dataset("titanic")

#basic plot graph
sns.catplot(x="sex",y="survived",hue="class", kind="bar",data=titanic)
plt.show

