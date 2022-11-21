const router = require('koa-router')()
const { parse } = require('csv-parse')
const { resolve } = require('path')
const fs = require('fs')
const Result = require('../model/Result')

router.prefix('/')


function parseCSV(hour) {
    const data = []
    let filePath = ''
    switch (hour) {
        case 0.5:
            filePath = resolve('backend/data/30MIN.csv')
            break
        case 24:
            filePath = resolve('backend/data/daily.csv')
            break
    }
    fs.createReadStream(filePath)
        .pipe(parse({ delimiter: ",", from_line: 2 }))
        .on("data", function (row) {
            const date = row[0]
            const price_open = Number(row[1])
            const price_high = Number(row[2])
            const price_low = Number(row[3])
            const price_close = Number(row[4])
            const volume_traded = Number(row[5])
            data.push([date, price_open, price_close, price_low, price_high, volume_traded])
        })
    return data
}

const dailyData = parseCSV(24)
const halfHourlyData = parseCSV(0.5)


function parseCSVLine(hour) {
    const data = []
    let filePath = ''
    switch (hour) {
        case 0.5:
            filePath = resolve('backend/data/30min-line.csv')
            break
        case 24:
            filePath = resolve('backend/data/daily-line.csv')
            break
    }
    fs.createReadStream(filePath)
        .pipe(parse({ delimiter: ",", from_line: 2 }))
        .on("data", function (row) {
            data.push([row[1], row[2]])
        })
    return data
}

const halfHourlyDataLine = parseCSVLine(0.5)
const dailyDataLine = parseCSVLine(24)


router.get('/candleData', async (ctx) => {
    let {timeInterval} = ctx.query
    timeInterval = Number(timeInterval)
    switch (timeInterval) {
        case 0.5:
            new Result(halfHourlyData, 'success').success(ctx)
            break
        case 24:
            new Result(dailyData, 'success').success(ctx)
            break
    }
})

router.get('/lineData', async (ctx) => {
    let {timeInterval} = ctx.query
    timeInterval = Number(timeInterval)
    switch (timeInterval) {
        case 0.5:
            new Result(halfHourlyDataLine, 'success').success(ctx)
            break
        case 24:
            new Result(dailyDataLine, 'success').success(ctx)
            break
    }
})

module.exports = router
