# xjson
----------
xjson 是一个能让你用xpath 语法来解析的json的工具

##Overview
----------

在处理json的时候，如果json 列表有很多元素的话，需要一个个迭代去处理。然而在xpath 却不是这样的，xpath 可以把路径下的都提取出来，这样就能把提取
变成一行，方便写在配置文件中。
xjson 做的就是这么一件事。让你能够以xpath的形式解析json。


    {
        "windowTitle":"Audi AUDI A8 - partslink24",
        "tcLinks":[
            {
                "caption":"2018",
                "gray":true,
                "jsonUrl":null,
                "selected":false,
                "subheader":false,
                "url":"group.action?catalogMarket=RDW&episType=771&familyKey=91155&lang=zh&localMarketOnly=true&modelYear=2018&ordinalNumber=2&partDetailsMarket=RDW&startup=false&mode=K00U0XXXX&upds=1147"
            },
            {
                "caption":"2017",
                "gray":true,
                "jsonUrl":null,
                "selected":false,
                "subheader":false,
                "url":"group.action?catalogMarket=RDW&episType=771&familyKey=91155&lang=zh&localMarketOnly=true&modelYear=2017&ordinalNumber=2&partDetailsMarket=RDW&startup=false&mode=K00U0XXXX&upds=1147"
            },
            {
                "caption":"2016",
                "gray":true,
                "jsonUrl":null,
                "selected":false,
                "subheader":false,
                "url":"group.action?catalogMarket=RDW&episType=771&familyKey=91155&lang=zh&localMarketOnly=true&modelYear=2016&ordinalNumber=2&partDetailsMarket=RDW&startup=false&mode=K00U0XXXX&upds=1147"
            }
        ]
    }


如果用json，需要把jsonurl 提取出来的话，需要



##Requirements
