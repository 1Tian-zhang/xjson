# xjson
----------
xjson 是一个能让你用xpath 语法来解析的json的工具

##Overview
----------

在处理json的时候，如果json 列表有很多元素的话，需要一个个迭代去处理。然而在xpath 却不是这样的，xpath 可以把路径下的都提取出来，这样就能把提取
变成一行，方便写在配置文件中。
xjson 做的就是这么一件事。让你能够以xpath的形式解析json。

    {
        "success":true,
        "message":"操作成功！",
        "result":[
            {
                "firstCategoryList":[
                    {
                        "name":"工具",
                        "id":"2"
                    }
                ],
                "secondCategoryList":[
                    {
                        "name":"钻削类电动工具",
                        "id":"142",
                        "list":[
                            {
                                "name":"手电钻",
                                "id":"925"
                            },
                            {
                                "name":"磁座钻",
                                "id":"928"
                            }
                        ]
                    },
                    {
                        "name":"磨削类电动工具",
                        "id":"143",
                        "list":[
                            {
                                "name":"角向磨光机",
                                "id":"936"
                            },
                            {
                                "name":"磨具电磨",
                                "id":"937"
                            }
                        ]
                    }
                ]
            }
        ]
    }


如果用json，需要把三级分类提取出来的话，你需要写成

	for result in json_content["result"]:
		for second_category in result["secondCategoryList"]:
			for third_category in second_category["list"]:
				print third_category["name"]
                
不仅混乱，而且需要时刻注意各层嵌套之间的关系，而在 xjson 中，你只需要按照层次关系写成
    
    result/secondCategoryList/list/name

就可以把三级分类全部提取出来了。
而且这样做的话，放在配置文件中，通过配置来提取json是非常方便的。

##Usage

	json_content = XJson()
	json_content.read_json(json_file_path)
	json_content.extract(...)
or 

	json_content = XJson(json_file_path)
	json_content.extract(...)
	
##Requirements

 - python2.7
 
