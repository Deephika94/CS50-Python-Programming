def filetype(nm):
    match nm:
        case "jpg" | "jpeg" | "gif" | "png":
            if nm == "jpg" or nm == "jpeg":
                print(f"image/jpeg")
            else:
                print(f"image/{nm}")
        case  "zip" | "pdf":
            print(f"application/{nm}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

def main():
    file = input("File name: ").strip().lower()
    names = file.split(".")
    filetype(names[-1])

main()