<template>
    <div>
        <img alt="AppTec logo" src="../assets/appTecLogo.png" height="100" style="vertical-align:left">
        <!-- <img alt="Bitcoin logo" src="../assets/bitcoinLogo.png" height="50" style="vertical-align:middle"> -->
        <br>
        <p>{{ chartMessage }}</p>
        <highcharts class="stock" :options="bitcoinOptions"></highcharts>
        <highcharts class="stock" :options="numpyOptions"></highcharts>
        <v-card height="150">
            <v-footer
                absolute
                class="font-weight-medium"
            >
                <v-col
                    class="text-center"
                    cols="12"
                >
                    {{ new Date().getFullYear() }} — <strong>Appliance Technologies</strong>
                </v-col>
            </v-footer>
        </v-card>
    </div>
    
</template>

<script>
import axios from 'axios';
import { stockChart } from 'highcharts-vue';

export default {
    name: 'Test',
    components: {
        highCharts: stockChart
    },
    data() {
        return {
            bitcoinPrices:[],
            chartMessage: "This is a chart showing the price of Bitcoin since January 1, 2020.",
            msg: 'Hello!',
            msg2:'',
            numpyOptions: {
                rangeSelector: {
                    selected: 1
                },
                title: {
                text: 'Numpy Array'
                },
                yAxis: {
                    title: {
                    text: 'Random Data Y'
                    },
                    plotLines: [{
                        value: 0,
                        width: 2,
                    }]
                },
                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'top',
                    x: -10,
                    y: 100,
                    borderWidth: 0
                },
                //series: results,
                series: [{
                    name: 'TEST DATA',
                    data: []
                }]
            },
            bitcoinOptions: {
                rangeSelector: {
                    selected: 1
                },
                title: {
                text: 'Bitcoin Price'
                },
                xAxis: {
                    type: 'datetime'
                },
                yAxis: {
                    title: {
                    text: 'MXN'
                    },
                    plotLines: [{
                    value: 0,
                    width: 1,
                    color: 'yellow'
                    }]
                },
                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'top',
                    x: -10,
                    y: 100,
                    borderWidth: 0
                },
                //series: results,
                series: [{
                    name: 'BTC',
                    data: [],
                    tooltip: {
                        valueDecimals: 2
                    }
                }]
            }
        };
    },
    methods: {
        getDataFromBack() {
            const path = 'http://localhost:5000/bitcoinPrices';
            axios.get(path)
                .then((res) => {
                    this.msg = res.data;
                    this.parseDataToArray();
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        getDataFromBack2() {
            const path = 'http://localhost:5000/numpyArray';
            axios.get(path)
                .then((res) => {
                    this.msg2 = res.data;
                    console.log(this.msg2)
                    // this.parseDataToArray();
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        parseDataToArray() {
            // MY ORIGINAL METHOD TO CONVERT AN OBJECT TO AN ARRAY (CAN HAVE ONLY VALUE)
            for(var propertyName in this.msg) {
                    //this.bitcoinPrices.push(this.msg[propertyName]);
                    this.bitcoinPrices.push([propertyName,this.msg[propertyName]]);
            }
            // USED THIS INSTEAD (WILL ALWAYS HAVE KEY-VALUE PAIR)
            // let bitcoinPricesObject = Object.entries(this.msg);
            // console.log(bitcoinPricesObject)
            // console.log(typeof bitcoinPricesObject)
            // this.bitcoinPrices = Array.from(bitcoinPricesObject)
            //
            //THIRD METHOD (JUST EXTRACTS PRICE AND IS IDENTIFIED BY NUMBER AND :)
            //this.bitcoinPrices = Object.keys(this.msg).map(i => this.msg[i])
            this.sendSeriesToData();
        },
        sendSeriesToData() {
            const series = this.$children[0].chart.series[0];
            series.setData(this.bitcoinPrices);
        }
    },
    created() {
        this.getDataFromBack();
        this.getDataFromBack2();
    },
    // mounted: function () {
    //     setTimeout(function(){ 
    //         //this.message = 'Data Fetched';
    //         this.chartOptions.series[0].data = [3, 5, 6, 9];
    //     }.bind(this), 3000);
    // }
};
</script>