from PIL import Image
import os

# 入力フォルダと出力フォルダのパス
input_folder = 'data\city0002\input'
output_folder = 'data\city0002\input-down'

# 出力フォルダが存在しない場合は作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 入力フォルダ内のすべてのファイルをループ処理
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # 画像ファイルのフルパス
        img_path = os.path.join(input_folder, filename)
        
        # 画像を開く
        with Image.open(img_path) as img:
            # 画像のサイズを取得
            width, height = img.size
            
            # 画像の横幅が1600ピクセル以上の場合に縮小
            if width > 1600:
                # 縮小後の高さを計算 (アスペクト比を維持)
                new_height = int((1600.0 / width) * height)
                
                # 画像をリサイズ
                img = img.resize((1600, new_height))
            
            # 変更した画像を出力フォルダに保存
            img.save(os.path.join(output_folder, filename))

print('すべての画像の処理が完了しました。')