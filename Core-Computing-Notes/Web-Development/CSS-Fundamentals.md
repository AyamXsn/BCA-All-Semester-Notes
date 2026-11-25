# CSS Fundamentals

## 1. CSS
CSS (Cascading Style Sheets) controls the presentation of HTML documents.

## 2. Rule structure
```css
p {
  color: #222;
  line-height: 1.5;
}
```
A rule contains a selector and declarations. Each declaration has a property and value.

## 3. Cascade and specificity
When declarations conflict, the cascade considers origin, importance, layer, specificity, and source order. Avoid excessive specificity and unnecessary `!important`.

## 4. Box model
The CSS box model includes content, padding, border, and margin. `box-sizing: border-box` makes declared width include padding and border.

## 5. Layout
Flexbox is useful for one-dimensional layout. Grid is useful for two-dimensional layout. Normal flow, positioning, and responsive media queries complete the layout toolkit.

## 6. Responsive design
Use fluid layouts, flexible images, and media queries to adapt to different viewport sizes. Test keyboard and touch interaction as well as visual appearance.

## 7. Exercise
Build a responsive navigation bar and a two-column layout that becomes one column on narrow screens.
