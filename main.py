from src.run import run


if __name__ == '__main__':
    zotero_api_key = "ci2jZjEI4Pv6HbpCU1ZogbIM"
    zotero_id = "16944485 "
    word_file_path = r"C:\Users\USER\Downloads\Telegram Desktop\water_mdpi.docx"
    new_file_path = r"C:\Users\USER\Downloads\Telegram Desktop\water_mdpi2.pdf"
    run(word_file_path, new_file_path, zotero_id, zotero_api_key, isNumbered=False, setColor=16711680, noUnderLine=True)
