// 読み込むjsonファイルを指定
const INPUT_FILE_NAME = 'runge_out.json';
// 描画するcanvas要素のidを指定
const CANVAS_ID = 'display';

document.addEventListener("DOMContentLoaded", function (event) {
  const canvasData = initCanvas(CANVAS_ID);
  drawAxis(canvasData);
  const ox = canvasData.oX;
  const oy = canvasData.oY;

  $('#draw').on('click', function () {
    $.getJSON(INPUT_FILE_NAME, function (data) {
      const ctx = canvasData.ctx;
      var m1x = 0;
      var m1y = 0;
      var m2x = 0;
      var m2y = 0;
      var m3x = 0;
      var m3y = 0;

      let timeKeys = [];

      Object.keys(data).forEach(function (key) {
        timeKeys.push(key);
      });

      var index = 0;
      setInterval(function () {
        let key = timeKeys[index];
        let value = data[key];

        m1x = ox + parseFloat(value.m1.x) * 100;
        m1y = oy - parseFloat(value.m1.y) * 100;
        render1(ctx, m1x, m1y);

        m2x = ox + parseFloat(value.m2.x) * 100;
        m2y = oy - parseFloat(value.m2.y) * 100;
        render2(ctx, m2x, m2y);

        m3x = ox + parseFloat(value.m3.x) * 100;
        m3y = oy - parseFloat(value.m3.y) * 100;
        render3(ctx, m3x, m3y);

        index++;
      }, 1);
    });
  });
});

// 渡されたcontextのx, yに四角を描画する
function render1(ctx, x, y) {
  ctx.beginPath();
  ctx.fillStyle = 'rgb(28, 5, 255)'; 
  ctx.fillRect(x, y, 3, 3);
}
function render2(ctx, x, y) {
  ctx.beginPath();
  ctx.fillStyle = 'rgb(255, 94, 25)';
  ctx.fillRect(x, y, 3, 3);
}
function render3(ctx, x, y) {
  ctx.beginPath();
  ctx.fillStyle = 'rgb(88, 191, 63)'; 
  ctx.fillRect(x, y, 3, 3);
}

// return canvasData:
//   ctx: canvasのcontext,
//   width: canvasのwidth,
//   height: canvasのheight,
//   oX: canvas上の原点のx座標,
//   oY: canvas上の原点のy座標,
function initCanvas(canvasId) {
  const cs = document.getElementById(canvasId);
  const ctx = cs.getContext('2d');
  const width = cs.width;
  const height = cs.height;

  const oX = Math.floor(width / 2);
  const oY = Math.ceil(height / 2);

  const canvasData = {
    ctx: ctx,
    width: width,
    height: height,
    oX: oX,
    oY: oY,
  }
  return canvasData;
}

// 引数: canvasData
// 座標軸の描画を行う
function drawAxis(cd) {
  cd.ctx.strokeStyle = '#999';
  cd.ctx.lineWidth = 1;

  // x座標軸を描画
  cd.ctx.beginPath();
  cd.ctx.moveTo(0, cd.oY);
  cd.ctx.lineTo(cd.width, cd.oY);
  cd.ctx.stroke();

  // y座標軸を描画
  cd.ctx.beginPath();
  cd.ctx.moveTo(cd.oX, 0);
  cd.ctx.lineTo(cd.oX, cd.height);
  cd.ctx.stroke();

  cd.ctx.fillStyle = "#999";

  // x座標軸の矢印を描画
  cd.ctx.beginPath();
  cd.ctx.moveTo(cd.width, cd.oY);
  cd.ctx.lineTo(cd.width - 10, cd.oY - 7);
  cd.ctx.lineTo(cd.width - 10, cd.oY + 7);
  cd.ctx.fill();

  // y座標軸の矢印を描画
  cd.ctx.beginPath();
  cd.ctx.moveTo(cd.oX, 0);
  cd.ctx.lineTo(cd.oX - 7, 10);
  cd.ctx.lineTo(cd.oX + 7, 10);
  cd.ctx.fill();

  // 原点を表す文字「Ｏ」を描画
  cd.ctx.beginPath();
  var maxWidth = 100;
  cd.ctx.font = "12px 'Verdana'";
  cd.ctx.textAlign = 'right';
  cd.ctx.fillText('Ｏ', cd.oX - 5, cd.oY + 15, maxWidth);
}
