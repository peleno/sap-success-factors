import axios from "axios";

const BaseRequest = axios.create({
    baseURL: "http://localhost:5000",
    responseType: "json",
});

export const getAllVacancies = async () => {
    const vacancies = await (await BaseRequest.get("/vacancy/")).data;
    return vacancies;
};

export const postNewVacancy = (vacancy) => {
    BaseRequest.post("/vacancy/", vacancy).then((response) => console.log(response));
};

export const deleteVacancy = async(vacancyId) => {
    BaseRequest.delete('/vacancy/' + vacancyId + '/');
};

export const updateVacancy = (vacancy) => {
    BaseRequest.put("/vacancy/", vacancy).then((response) => console.log(response));
};

// export const getSensorRecordsForRobot = async (robotId) => {
//     const records = await (
//         await BaseRequest.get(`/robot/${robotId}/monitor`)
//     ).data;
//     console.log(records);
//     return records;
// };
