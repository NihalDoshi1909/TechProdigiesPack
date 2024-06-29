const expr=require("express")
const app=expr()
const path=require("path")
const cp=require("cookie-parser")
app.use(cp())

app.use(expr.static("../public"))
// app.use(expr.static("../public",{index:"SignUp.html"}))
app.use('/js', expr.static(path.join(__dirname)))


app.get("/SignUp",(req,res)=>{
    [fname,lname,gender,age,weight,height,contact]=req.query
    res.redirect("/profile.html")
})
app.get("/profile",(req,res)=>{
    res.write(`
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello ${fname}</h1>
</body>
</html>`)

res.send()
})

app.listen(3000)