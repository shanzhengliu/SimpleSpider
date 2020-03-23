#SimpleSpider Instruction
##Using in command
There are 7 argument when you use in the command.

| argument | type |default|desctipyion|
| --- | --- | --- |---|
|url|str|None|Your url
single|bool|True|If you want to use script to get the content from series of page,you can set it as False and se the index. 
|re|str|None|Regular Expression setting use,dont forget to use "" ,eg: --re "ab*c"
|xpath|str|None|Xpath setting use, dont forget to use "",eg:--xpath "//*div[0]/text()"
|index|str|default|use "," to spite the index, eg --index  1,2,3,4,5,6,7
|print|bool|True| if you dont want to print out it in the console,set it as False
|output|str|None| if you want to export your result, use it to set the path,eg: --output "D:/data.xlsx."

Example 1:
get the data with Regular Expression from single Page.
```
python SimpleSpider.py --url https://www.163.com --re "<title>(.*.?)</title>"
```

output:
```['网易']```

Example 2:
get the data with Xpath from single Page
```python SimpleSpider.py --url https://www.163.com --xpath "//title/text()"```

output:
```['网易']```

Example 3:
get the data with Xpath from mulitiple Page
```python SimpleSpider.py --url https://ent.163.com/20/0323/ --re "<title>(.*.?)</title>" --single False --index 08/F8D2BVI700038FO9.html,10/F8D8B35800038FO9.html```

output:
```[['疫情期间还出游？网友在巴厘岛偶遇霍建华林心如_网易娱乐'], ['台湾女星刘真去世：上《康熙》走红 当郭台铭红娘_网易娱乐']]```



If you want to use the function in this model,you just need to:
```import SimpleSpider```

