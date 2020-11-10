# capture
This script based on python3, use a capture code to download the English daily sentence and its Chinese translation from iciba:金山词霸
This data download by day, so you can set which day you get start and last days, then the script can download them automatic,and store with a text file in the same path with this script.

The website response a json format array. Here is the list:

            传入参数：
            file //数据格式，默认（json），可选xml
            date //标准化日期格式 如：2013-05-06， 如：http://open.iciba.com/dsapi/?date=2013-05-03
            如果 date为空 则默认取当日的，当日为空 取前一日的
            type(可选) // last 和 next 你懂的，以date日期为准的，last返回前一天的，next返回后一天的

            JSON 字段解释
            {
            'sid':'' #每日一句ID
            'tts': '' #音频地址
            'content':'' #英文内容
            'note': '' #中文内容
            'love': '' #每日一句喜欢个数
            'translation':'' #词霸小编
            'picture': '' #图片地址
            'picture2': '' #大图片地址
            'caption':'' #标题
            'dateline':'' #时间
            's_pv':'' #浏览数
            'sp_pv':'' #语音评测浏览数
            'tags':'' #相关标签
            'fenxiang_img':'' #合成图片，建议分享微博用的
            }
