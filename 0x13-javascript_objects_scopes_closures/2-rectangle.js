#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0)) {
      return this;
    }
    if ((typeof w === 'undefined') || (typeof h === 'undefined')) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
