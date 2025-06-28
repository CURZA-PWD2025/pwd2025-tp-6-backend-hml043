import './assets/main.css'

import { createApp } 	from 'vue'
import { createPinia } 	from 'pinia'

import App 		from './App.vue'
import router 	from './router'

const app = createApp(App)

app.config.globalProperties.$filters = {
	truncateText(text: string, maxLength: number) {
    	return text.length <= maxLength ? text : text.slice(0, maxLength) +' …';
  	},
  	currency(value:number) {
  		return value.toFixed(2).toLocaleString("de-DE") +" $";
	},
	capitalize(value) {
        if (!value) return '';
        return value.charAt(0).toUpperCase() + value.slice(1);
    },
    formatNumberWithCommas(num:number, length:number):string {
    	const numStr 	= num.toString();
    	const parts 	= numStr.split(',');
    	let integerPart = parts[0];
    	const decimalPart = parts.length > 1 ? ',' + parts[1] : '';

    	// Regex to add commas to the integer part
    	// It looks for a digit followed by groups of three digits that are not at the end of the string
    	const formattedIntegerPart = integerPart.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    	let aux = formattedIntegerPart + decimalPart;

    	const zerosNeeded = length - aux.length;
  		if (zerosNeeded > 0) {
    		aux = " ".repeat(zerosNeeded) + aux;
  		}

    	return aux;
	}
};

app.use(createPinia())
app.use(router)

app.mount('#app')
