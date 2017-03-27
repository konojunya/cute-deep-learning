# cute-deep-learning
女の子の自撮りをただひたすら眺めるアプリの可愛いか判定用のニューラルネットワーク

## 分類の仕方

- 可愛い女の子:1000枚
- 可愛くない女の子:1000枚

の画像を用意。

1. データセットとして扱うので顔を認識して、切り取る(OpenCV)
2. 教師データとして読み込む
3. 深層学習
4. グラビアアイドルの写真がどっちの分類にはいるのかを深層学習で判別
5. 可愛い女の子だけのリストを作成する