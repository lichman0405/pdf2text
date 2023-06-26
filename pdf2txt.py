# 导入需要的模块
import pdfminer.high_level
import os

# 定义一个函数，用于从PDF文件中提取文本
def extract_text_from_pdf(pdf_file):
    # 使用pdfminer.high_level.extract_text函数，将PDF文件中的文本保存到一个字符串中
    text = pdfminer.high_level.extract_text(pdf_file)
    # 返回文本字符串
    return text

# 定义一个函数，用于将文本保存到txt文件中
def save_text_to_txt(text, txt_file):
    # 打开txt文件，以写入模式
    with open(txt_file, "w", encoding="utf-8") as f:
        # 写入文本
        f.write(text)

# 定义一个函数，用于处理一个PDF文件夹，将其中的所有PDF文件转换为txt文件，并保存在另一个文件夹中
def process_pdf_folder(pdf_folder, txt_folder):
    # 遍历PDF文件夹中的所有文件
    for file in os.listdir(pdf_folder):
        # 如果是PDF文件，就处理它
        if file.endswith(".pdf"):
            # 拼接完整的PDF文件路径
            pdf_file = os.path.join(pdf_folder, file)
            # 拼接完整的txt文件路径，使用相同的文件名，但是后缀改为.txt
            txt_file = os.path.join(txt_folder, file[:-4] + ".txt")
            # 提取PDF文件中的文本
            text = extract_text_from_pdf(pdf_file)
            # 将文本保存到txt文件中
            save_text_to_txt(text, txt_file)

# 定义PDF文件夹的路径，可以根据需要修改
pdf_folder = "/home/pdf2txt/inputpdf"
# 定义txt文件夹的路径，可以根据需要修改
txt_folder = "/home/pdf2txt/output"
# 调用函数，处理PDF文件夹
process_pdf_folder(pdf_folder, txt_folder)
