import AsciiPy

text = AsciiPy.AsciiText.GenerateText("Rayan", "graffiti")
print(text)
lst = AsciiPy.AsciiText.FontList()
print(lst)
img = AsciiPy.AsciiImage.GenerateFromPath("python-logo.png")
print(img)
out = AsciiPy.AsciiImage.GenerateFromUrl("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
print(out)

if __name__ == "__main__":
    AsciiPy.AsciiImage.VideoFromPath("images-videos/cube.mp4")
