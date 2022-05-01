const timelineData = [
{
  text: '大学入学',
  date: '2019-09-01',
  category: {
    tag: 'Ⅰ',
    color: '#FFDB14' },

  link: {
    url: 'https://www.bilibili.com/',
    text: '了解详情' } },


{
  text: '开始接触各种编程语言',
  date: '2019-10-01',
  category: {
    tag: 'Ⅱ',
    color: '#e17b77' },

  link: {
    url: 'https://www.bilibili.com/',
    text: '了解详情' } },


{
  text: '疫情在加自学各种计算机基础知识',
  date: '2020-01-07',
  category: {
    tag: 'Ⅲ',
    color: '#1DA1F2' },

  link: {
    url: 'https://www.bilibili.com/',
    text: '了解详情' } },


{
  text:
  '参加校比赛获奖',
  date: '2020-10-01',
  category: {
    tag: 'Ⅳ',
    color: '#018f69' },

  link: {
    url:'https://www.bilibili.com/',
    text: '了解详情' } },


{
  text: '参加实习',
  date: '2022-06-01',
  category: {
    tag: 'Ⅴ',
    color: '#018f69' },

  link: {
    url: 'https://www.bilibili.com/',
    text: '了解详情' } }];




const TimelineItem = ({ data }) => /*#__PURE__*/
React.createElement("div", { className: "timeline-item" }, /*#__PURE__*/
React.createElement("div", { className: "timeline-item-content" }, /*#__PURE__*/
React.createElement("span", { className: "tag", style: { background: data.category.color } },
data.category.tag), /*#__PURE__*/

React.createElement("time", null, data.date), /*#__PURE__*/
React.createElement("p", null, data.text),
data.link && /*#__PURE__*/
React.createElement("a", {
  href: data.link.url,
  target: "_blank",
  rel: "noopener noreferrer" },

data.link.text), /*#__PURE__*/


React.createElement("span", { className: "circle" })));




const Timeline = () =>
timelineData.length > 0 && /*#__PURE__*/
React.createElement("div", { className: "timeline-container" },
timelineData.map((data, idx) => /*#__PURE__*/
React.createElement(TimelineItem, { data: data, key: idx })));




const App = () => /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/
React.createElement("h1", null, "大学生涯时间轴"), /*#__PURE__*/
React.createElement(Timeline, null));


ReactDOM.render( /*#__PURE__*/React.createElement(App, null), document.getElementById('app'));