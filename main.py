import random
import tweepy

def tweet_bot():

    chest_list = ["ひざつきプッシュアップ","プッシュアップ","インクラインプッシュアップ","ヒンズープッシュアップ","ツイストプッシュアップ" \
        ,"ダイアモンドプッシュアップ", "チェストプレスパルス", "腕開いてとじるやつ", "肘と肘くっつけるやつ", "サイドプッシュアップ"]
    core_list = ["ロシアンツイスト","サイドベント","グッドモーニング","プランク","ニートゥチェスト","マウンテンクライマー" \
        ,"ｽﾜｲｼｮｳ","ヒールタッチ","クロスオーバークランチ","サイドブリッジ","Vアップ","サイドプランク","シットアップ","バイシクルクランチ" \
                 ,"ヒップリフトブリッジ","サイドステップブリッジ","バックエクステンション","ライイングアームサークル","膝コロ"]
    leg_list = ["ワイドスクワット","ヒップリフト","レッグアダクション","ドンキーキック","ファイヤーハイドラント","サイドランジ","足パカ" \
        ,"レッグアブダクション","レインボーレッグリフト"]

    chest = chest_list[random.randint(0, len(chest_list) - 1)]
    core = core_list[random.randint(0, len(core_list) - 1)]
    leg = leg_list[random.randint(0, len(leg_list) - 1)]

    ck = 'cxzvVLA8B3IZxxyyZsM8w4Bik'
    cs = 'fALALJLBYi4pBSsFx8d5LNyH8QXK0mX69QNudoGq8CVsFWRtdc'
    at = '1135810742685331458-dvdQ6Qc9qTh0AUiQOPmqnFElkNzqnZ'
    ats = 'a6OKp7DD2vH4H8iLnKCn5AbeoLy4cGEXgQvcnxuWoCDPk'

    client = tweepy.Client(consumer_key=ck, consumer_secret=cs, access_token=at, access_token_secret=ats)

    # パラメータ名を省略したい場合
    # client = tweepy.Client(None, ck, cs, at, ats)

    tweettext = chest + "\n" + core + "\n" + leg;
    client.create_tweet(text=tweettext)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tweet_bot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
