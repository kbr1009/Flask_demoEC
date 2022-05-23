function saveDate() {
  var day = new Date();
  localStorage.setItem('year',day.getFullYear() + '年');
  localStorage.setItem('month',(day.getMonth()+1) + '月');
  localStorage.setItem('date',day.getDate() + '日');
  localStorage.setItem('time',day.getHours() + '時' + day.getMinutes() + '分' + day.getSeconds() + '秒');
}

function displayDate() {
  var year = localStorage.getItem('year');
  var month = localStorage.getItem('month');
  var date = localStorage.getItem('date');
  var time = localStorage.getItem('time');
  
  if(year) {
    var message = 'あなたは' + year + month + date + time + 'にこの記事を読みました';
    alert(message);
  } else {
    alert('日付を記録してください');
  }
}

function storageClear() {
  localStorage.removeItem('year');
  localStorage.removeItem('month');
  localStorage.removeItem('date');
  localStorage.removeItem('time');
}
