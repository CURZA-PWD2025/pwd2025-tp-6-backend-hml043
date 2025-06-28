export function currency(value) {
	return value.toFixed(2).toLocaleString() + " $";	
}

export function truncateText(text, maxLength) {
	return text.length <= maxLength ? text : text.slice(0, maxLength) + ' …';
}