from lxml import html

with open("./basic-xpath.html") as basic_regex_file:
    document = html.fromstring(basic_regex_file.read())

    print(document.xpath(r"""//div[3]/text()""")[0].strip())

