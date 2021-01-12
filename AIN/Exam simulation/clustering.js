const printDistance = true; //print the distance from centroids


function getCentroid(points) {
  let sumx = 0;
  let sumy = 0;

  points.forEach((p) => {
    sumx += p[0];
    sumy += p[1];
  });
  /*
    console.log(
      `New Centroid: [${parseFloat(sumx) / points.length}, ${
        parseFloat(sumy) / points.length
      }]`
    );
  */
  return [parseFloat(sumx) / points.length, parseFloat(sumy) / points.length];
}

function distance(points, centroids, distanceFunction) {
  let dic = new Map();
  centroids.forEach((c) => {
    dic.set(c, []);
  });

  points.forEach((point) => {
    let px = point[0];
    let py = point[1];
    let closestCentroid = centroids[0];
    let smallestDistance = Number.MAX_SAFE_INTEGER;

    centroids.forEach((centroid) => {
      let cx = centroid[0];
      let cy = centroid[1];

      let dist = distanceFunction(cx, cy, px, py);

      if (printDistance)
        console.log(
          `Distance from [${px},${py}] to centroid [${cx}, ${cy}] = ${dist}`
        );

      if (dist < smallestDistance) {
        smallestDistance = dist;
        closestCentroid = centroid;
      }
    });

    let newArray = [...dic.get(closestCentroid)];
    newArray.push(point);

    dic.set(closestCentroid, newArray);
  });

  console.log(dic);
  return dic;
}

function clustering(points, centroids, distanceFunction) {
  let i = 1;

  console.log("ITERATION: ", i);
  let dic = distance(points, centroids, distanceFunction);
  let done = false;
  while (!done) {
    let oldCentroids = Array.from(dic.keys());
    let newCentroids = [];
    oldCentroids.forEach((oldCentroid) => {
      let newCentroid = getCentroid(dic.get(oldCentroid));
      if (
        newCentroid[0] == oldCentroid[0] &&
        newCentroid[1] == oldCentroid[1]
      ) {
        done = true;
      } else {
        newCentroids.push(newCentroid);
      }
    });
    if (!done) {
      console.log("ITERATION: ", ++i);
      dic = distance(points, newCentroids, distanceFunction);
    }
  }
  console.log("END! FINAL CLUSTERS:\n", dic);
}

function median(points, centroids) {
  return clustering(
    points,
    centroids,
    (cx, cy, px, py) => Math.abs(cx - px) + Math.abs(cy - py)
  );
}
function mean(points, centroids) {
  return clustering(
    points, 
    centroids, 
    (cx, cy, px, py) => Math.hypot(cx - px, cy - py)
  );
}


//! CHANGE BELOW
const points = [
  [3, 4],
  [4, 2],
  [1, 2],
  [1, 1],
  [1, 3],
];

const centroids = [
  [1, 1],
  [2, 4],
];


mean(points, centroids);
// median(points, centroids);