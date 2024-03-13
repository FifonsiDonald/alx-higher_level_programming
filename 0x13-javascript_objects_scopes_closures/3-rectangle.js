#!/usr/bin/node

module.exports = class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	prints(){
		let x;
		for (let i = 0; i < this.height; i++) {
			x = '';
			for (let j = 0; j < this.width; j++) {
				x += 'X';
			}
			console.log(x);
		}
	};
