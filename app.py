import PyPDF2


def pdf_to_text(file_path):
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() or ""
    except FileNotFoundError:
        print("The file was not found.")
    except PyPDF2.errors.PdfError:
        print("Error reading the PDF file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return text


def main():
    file_path = input("Enter the path to the PDF file: ")
    text = pdf_to_text(file_path)
    if text:
        output_file = file_path.replace(".pdf", ".txt")
        with open(output_file, "w") as text_file:
            text_file.write(text)
        print(f"Text successfully extracted to {output_file}")


if __name__ == "__main__":
    main()
