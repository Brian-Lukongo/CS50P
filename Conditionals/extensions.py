# The program will ask the user to enter a file name. If the file name ends with .gif, the program will output image/gif. If the file name ends with .jpg or .jpeg, the program will output image/jpeg. If the file name ends with .png, the program will output image/png. If the file name ends with .pdf, the program will output application/pdf. If the file name ends with .txt, the program will output text/plain. If the file name ends with .zip, the program will output application/zip. Otherwise, the program will output application/octet-stream.
file_name = input("What is the name of the file? ").strip().lower()

if file_name.endswith(".gif"): 
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith("jpeg"):
    print("image/jpeg")
elif file_name.endswith("png"):
    print("image/png")
elif file_name.endswith("pdf"):
    print("application/pdf")
elif file_name.endswith("txt"):
    print("text/plain")
elif file_name.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")