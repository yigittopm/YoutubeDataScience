import pandas as pd

df = pd.read_csv("USvideos.csv")
result = df.head(10)
result = len(df.columns)
result = df.tail()
result = df.columns

# bazı kolonları siliyoruz
df = df.drop(['comments_disabled','thumbnail_link','ratings_disabled',
       'video_error_or_removed','description','trending_date'],axis=1)

result = df
result = df["likes"].mean() # Beğeni ortalaması
result = df.head(10)[["title","likes","dislikes"]] # ilk 50 title-likes-dislike
result = df[(df["views"].max()) == df["views"]][["title","views"]] #max izlenen video
result = df[(df["views"].min()) == df["views"]][["title","views"]] #min izlenen video
result = df.sort_values("views",ascending=False).head(10)[["title","views"]]
result = df.groupby("category_id").mean().sort_values("likes")[["likes","views"]]
df["yorum"] = len(df["comment_count"])
result = df[["title","yorum"]]
print(result)