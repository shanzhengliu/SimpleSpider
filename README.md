# SimpleSpider Instruction

This is a module to help you use network spider easier.
## How to install 

```pip install SimpleSpider```

## Using in command
There are 8 argument when you use in the command.

| argument | type |default|desctipyion|
| --- | --- | --- |---|
|url|str|None|Your url
single|bool|True|If you want to use script to get the content from series of page,you can set it as False and se the index. 
|re|str|None|Regular Expression setting use,dont forget to use "" ,eg: --re "ab*c"
|xpath|str|None|Xpath setting use, dont forget to use "",eg:--xpath "//*div[0]/text()"
|index|str|default|use "," to spite the index, eg --index  1,2,3,4,5,6,7
|print|type=bool|True| if you dont want to print out it in the console,set it as False
|output|type=str|None| if you want to export your result, use it to set the path,eg: --output "D:/data.xlsx."
|mode|tpye=str|None|you can use "img", "xp" and "re" to set mode get img urls,or use xpath, or regular expression

Example 1:
get the data with Regular Expression from single Page.  
```
SimpleSpider --mode re --url https://www.163.com --re "<title>(.*.?)</title>"
```

output:
```网易```

Example 2:
get the data with Xpath from single Page  
```SimpleSpider --mode xp--url https://www.163.com --xpath "//title/text()"```

output:  
```网易```

Example 3:
get the data with Xpath from mulitiple Page  
```SimpleSpider --mode xp --url https://ent.163.com/20/0323/ --re "<title>(.*.?)</title>" --single False --index 08/F8D2BVI700038FO9.html,10/F8D8B35800038FO9.html```

output:  
```'疫情期间还出游？网友在巴厘岛偶遇霍建华林心如_网易娱乐'```  
```'台湾女星刘真去世：上《康熙》走红 当郭台铭红娘_网易娱乐'```


Example 4:
get the data with Xpath from single Page  
```SimpleSpider --mode img --url https://www.baidu.com ```

output:  
```//www.baidu.com/img/gs.gif```

## If you want to use the function in this model,you just need to:
```from SimpleSpider import SimpleSpider```

there are some function for you to simply the code  
Example 1:

```result = SinglePageGetByRegEx(Url=http://www.163.com,Re="<title>(.*?.)")```  
the value of result is ```['网易']```

Example 2:
```List = [53,54,55,56]  ```  
```result = MulityPageGetByRegEx(Url="http://www.oursteps.com.au/bbs/forum.php?mod=forumdisplay&fid=", IndexList=List,RegEx="<title>(.*?.)</title>")``` 
the value of result is   
```[['生活其他 -  新足迹 - 新足迹澳洲华人生活大全'], ['证券外汇 - 新足迹澳洲华人生活大全'], ['个人理财 - 新足迹澳洲华人生活大全'], ['生意种种 - 新足迹澳洲华人生活大全']]```

Xpath and Regular Expression are avaluable to be used.

also you can directly get the middle string in a page.
Example 3:
the html page is  
```
<html>
<title>网易</title>
</html>  
```
   
```result = SinglePageGetMiddleStr(http://www.163.com,front="<title>,back="</title>")```  
output  
```['网易']```

also you can directly get the image in a page.
```result = SinglePageGetImgUrl(http://www.baidu.com")```   
output  
```//www.baidu.com/img/gs.gif```   

if you want to know more, please visit : https://github.com/shanzhengliu/SimpleSpider






