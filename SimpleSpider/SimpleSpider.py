import requests
from lxml import etree
import re
import xlwt
#SinglePageXpath

def SinglePageGetByXpath(Url,Xpath,Header=False,Cookie=False):
    if(Header==False):
        if(Cookie==False):
            result = requests.get(Url)
        else:
            result = requests.get(Url,cookies=Cookie)
    else:
        if(Cookie==False):
            result = requests.get(Url, headers=Header)
        else:
            result = requests.get(Url, cookies=Cookie,headers=Header)
    html = etree.HTML(result.text)
    XpathResult = html.xpath(Xpath)
    return XpathResult

#MuiltyPage For Simple Index
#eg.https://aaa.com.cc?page=1,  1 is index, you can init a list [1,2,3,4,5]


def MulityPageGetByXpath(Url,IndexList,Xpath,Header=False,Cookie=False):
    resultList = []
    for i in IndexList:
        if(Header==False):
            if(Cookie==False):
                result = requests.get(Url + str(i))
            else:
                result = requests.get(Url + str(i),cookies=Cookie)
        else:
            if(Cookie==False):
                result = requests.get(Url+str(i),headers=Header)
            else:
                result = requests.get(Url + str(i), headers=Header,cookies=Cookie)
        html = etree.HTML(result.text)
        XpathResult = html.xpath(Xpath)
        resultList.append(XpathResult)

    return resultList




#SinglePageXpath Post

def SinglePagePostByXpath(Url,Xpath,Para,Header=False,Cookie=False):
    if(Header==False):
        if(Cookie==False):
            result = requests.post(Url,data = Para)
        else:
            result = requests.post(Url,cookies=Cookie,data = Para)
    else:
        if(Cookie==False):
            result = requests.post(Url, data=Para,headers=Header)
        else:
            result = requests.post(Url, data=Para, headers=Header,cookies=Cookie)
    html = etree.HTML(result.text)
    XpathResult = html.xpath(Xpath)
    return XpathResult

#SingleMulityXpath Post
def MulityPagePostByXpath(Url,IndexList,Para,Xpath,Header=False,Cookie=False):
    resultList = []
    for i in IndexList:
        if(Header==False):
            if(Cookie==False):
                result = requests.post(Url + str(i),data=Para)
            else:
                result = requests.post(Url + str(i),data=Para,cookies=Cookie)
        else:
            if(Cookie==False):
                result = requests.post(Url+str(i),data=Para,headers=Header)
            else:
                result = requests.post(Url + str(i), data=Para,headers=Header,cookies=Cookie)
        html = etree.HTML(result.text)
        XpathResult = html.xpath(Xpath)
        resultList.append(XpathResult)

    return resultList




#SinglePageRegEx

def SinglePageGetByRegEx(Url,RegEx,Header=False,Cookie=False):
    if(Header == False):
        if(Cookie==False):
            result = requests.get(Url)
    else:
        if(Cookie==False):
            result = requests.get(Url,headers=Header)
        else:
            result = requests.get(Url,headers=Header,cookies=Cookie)
    pattern = re.compile(RegEx)
    RegExResult = pattern.findall(result.text)
    return RegExResult

#MuiltyPageGetRegEx
def MulityPageGetByRegEx(Url,IndexList,RegEx,Header=False,Cookie=False):
    resultList = []
    for i in IndexList:
        if(Header==False):
            if(Cookie==False):
                result = requests.get(Url + str(i))
            else:
                result = requests.get(Url + str(i), cookies=Cookie)
        else:
            if(Cookie==False):
                result = requests.get(Url+str(i), headers=Header)
            else:
                result = requests.get(Url+str(i), headers=Header,cookies=Cookie)
        pattern = re.compile(RegEx)
        RegExResult = pattern.findall(result.text)
        resultList.append(RegExResult)
    return resultList



#SinglePagePost
def SinglePagePostByRegEx(Url,RegEx,Para,Header=False,Cookie=False):
    if(Header==False):
        if(Cookie==False):
            result = requests.post(Url,data = Para)
        else:
            result = requests.post(Url,cookies=Cookie,data = Para)
    else:
        if(Cookie==False):
            result = requests.post(Url, data=Para,headers=Header)
        else:
            result = requests.post(Url, data=Para, headers=Header,cookies=Cookie)
    pattern = re.compile(RegEx)
    RegExResult = pattern.findall(result.text)
    return RegExResult



#MuiltyPagePost
def MulityPagePostByRegEx(Url,IndexList:list,Para,RegEx,Header=False,Cookie=False):
    resultList = []
    for i in IndexList:
        if(Header==False):
            if(Cookie==False):
                result = requests.post(Url + str(i),data=Para)
            else:
                result = requests.get(Url + str(i), cookies=Cookie,data=Para)
        else:
            if(Cookie==False):
                result = requests.post(Url+str(i), headers=Header,data=Para)
            else:
                result = requests.post(Url+str(i), headers=Header,cookies=Cookie,data=Para)
        pattern = re.compile(RegEx)
        RegExResult = pattern.findall(result.text)
        resultList.append(RegExResult)
    return resultList

def SinglePageGetMiddleStr(Url,front,back,Header=False,Cookie=False):
    if(Header == False):
        if(Cookie==False):
            result = requests.get(Url)
    else:
        if(Cookie==False):
            result = requests.get(Url,headers=Header)
        else:
            result = requests.get(Url,headers=Header,cookies=Cookie)
    RegEx = front + "(.*?)" + back
    pattern = re.compile(RegEx)
    RegExResult = pattern.findall(result.text)
    return RegExResult

#getMiddleThingMulty
def MulityPageGetMiddleStr(Url,IndexList,front,back,Header=False,Cookie=False):
    resultList = []
    for i in IndexList:
        if(Header==False):
            if(Cookie==False):
                result = requests.get(Url + str(i))
            else:
                result = requests.get(Url + str(i), cookies=Cookie)
        else:
            if(Cookie==False):
                result = requests.get(Url+str(i), headers=Header)
            else:
                result = requests.get(Url+str(i), headers=Header,cookies=Cookie)
        RegEx = front+"(.*?)"+back
        pattern = re.compile(RegEx)
        RegExResult = pattern.findall(result.text)
        resultList.append(RegExResult)
    return resultList


def SinglePagePostMiddleStr(Url,Para,front,back,Header=False,Cookie=False):
    if(Header == False):
        if(Cookie==False):
            result = requests.get(Url,data=Para)
        else:
            result = requests.get(Url, data=Para,cookies=Cookie)
    else:
        if(Cookie==False):
            result = requests.get(Url,headers=Header,data=Para)
        else:
            result = requests.get(Url,headers=Header,data=Para,cookies=Cookie)
    RegEx = front + "(.*?)" + back
    pattern = re.compile(RegEx)
    RegExResult = pattern.findall(result.text)
    return RegExResult



#ExportFile
def ExportFileToExcel(data:list,FlieName="data.xlsx"):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('table1', cell_overwrite_ok=True)

    for i in range(0,len(data),1):
        sheet1.write(i, 0, data[i])
    f.save(FlieName)

import logging
import json
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, default=None)
    parser.add_argument("--single",type=bool, default=True)
    parser.add_argument('--re', type=str, default=None)
    parser.add_argument('--xpath', type=str, default=None)
    parser.add_argument('--index', type=str, default=None)
    parser.add_argument('--print', type=bool, default=True)
    parser.add_argument('--output',type=str, default=None )

    args = parser.parse_args()

    if(args.single==True):
            if(args.re!=None):
                result=SinglePageGetByRegEx(Url=args.url,RegEx=args.re)
                if(args.print==True):
                    print(result)
                if (args.output != None):
                    ExportFileToExcel(result, args.output)

            else:
                result=SinglePageGetByXpath(Url=args.url,Xpath=args.xpath)
                if (args.print == True):
                    print(result)

                if(args.output!=None):
                    ExportFileToExcel(result,args.output)
    else:
        indexlist = str(args.index).split(",")
        if (args.re != None):

            result = MulityPageGetByRegEx(Url=args.url, IndexList=indexlist, RegEx=args.re)
            if (args.print == True):
                print(result)
            if (args.output != None):
                ExportFileToExcel(result, args.output)
        else:
            result = MulityPageGetByXpath(Url=args.url, IndexList=indexlist, RegEx=args.re)
            if (args.print == True):
                print(result)
            if (args.output != None):
                ExportFileToExcel(result, args.output)

