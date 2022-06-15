// import React, { useEffect, useState } from "react";

// import { useHistory } from "react-router-dom";
// import { getSensorRecordsForRobot } from "../api/Api";
// const MonitoringRecord = ({ record }) => {
//     console.log("record: " + record);

//     const { timestamp, speed, battery, latitude, longitude, temperature } =
//         record;
//     return (
//         <div>
//             {timestamp}, {speed}, {battery}, {latitude}, {longitude},{" "}
//             {temperature}
//         </div>
//     );
// };

// export const RobotMonitoring = () => {
//     const history = useHistory();
//     const robot = history.location.state;
//     const [sensorRecords, setSensorRecords] = useState([]);

//     useEffect(() => {
//         getSensorRecordsForRobot(robot.id).then((res) => setSensorRecords(res));
//     }, []);
//     return (
//         <div>
//             <div>{robot.name}</div>
//             {sensorRecords.map((record) => (
//                 <MonitoringRecord record={record}></MonitoringRecord>
//             ))}
//             {sensorRecords.map((record) => console.log(record))}
//         </div>
//     );
// };
