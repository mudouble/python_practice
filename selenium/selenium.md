## 常见用法
1. 重复性任务：下载网站，或者日志记录，提交表单，可以在预设的时间内创建一个selenium脚本执行一个服务
2. 网页爬虫：如果某个网站不提供api，selenium可以不使用api收集数据，但是某些网站会屏蔽selenium
3. 测试：使用selenium做测试需要在selenium执行操作后进行断言，所以一个好的断言类库是至关重要的

断言
- 断言assertion，是一种验证程序在运行时是否符合预期行为的机制，通常用于调试和测试阶段。
- 
`x = 5
assert x > 0, "x should be greater than 0"`

test Runner
- 一个用于执行测试用例并生成测试报告的工具，在测试中，TestRunner通常与测试框架（unittest，pytest，junit等）结合使用，帮助自动测试的执行和管理

浏览器选项
- browserName
- browserVersion
- pageLoadStrategy

远程webdriver的作用远程操作浏览器下载文档，发送命令等
针对不同的浏览器有不同的特定功能


与元素交互
1. 点击适用于任何元素
2. 发送键位 仅适用于文本字段和内容可编辑元素
3. 清除 仅适用于文本字段和内容可编辑元素
4. 提交 仅适用于表单元素
5. 选择 

每个浏览器都有自己的一套开发者工具 Chrome DevTools CDP协议，selenium
试图实现一种基于标准的，跨浏览器， 稳定的CDP替代方案BiDi，BiDi可以允许直接与浏览器的DevTools协议进行交互，从而实现更加高级的功能，如网络监控，性能分析，JavaScript调试的

Grid可以在多台计算机并行运行测试