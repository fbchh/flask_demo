"""
文件上传demo
"""
import os
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename

# 基础配置
upload_file_dir = r"D:\CODE_AND_CODETOOLS\CODE\SOURCE_TREE\flask_demo\flask_hello\upload_file"
upload_file_config_nm = "upload_file_dir"

upload_obj = Flask(__name__)
upload_obj.config[upload_file_config_nm] = upload_file_dir


@upload_obj.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    """
    文件上传 视图函数
    """
    if request.method == "POST":
        # todo:文件合理性验证
        ...

        file = request.files.get("file", None)  # 这里的nm和html中上传文件的地方的name一致
        if file:
            try:
                origin_filename = secure_filename(file.filename)
                # print(origin_filename, upload_obj.config[upload_file_config_nm])
                file.save(os.path.join(upload_obj.config[upload_file_config_nm], origin_filename), buffer_size=1024)
                # todo: 返回上传成功的“消息/反馈”
                return f"{origin_filename} 上传成功"
            except Exception as e:
                print(f"文件上传失败:{e}")

    return render_template("upload_file.html")  # template目录下


if __name__ == "__main__":
    upload_obj.run()
