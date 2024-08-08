import faculties from '../../../../public/db_faculties.json';

const PROCENT_MAX = 80.0;

export const startQuiz = (setQuestions, setStartNewQuiz) => {
    // Проверка наличия данных о факультетах
    if (!faculties || !faculties.faculties) {
        console.error('Faculties data is not available.');
        return;
    }

    // Сохраняем факультеты в localStorage
    localStorage.setItem('faculties', JSON.stringify(faculties.faculties));

    // Получаем все вопросы из всех факультетов
    const allQuestions = faculties.faculties.reduce((acc, faculty) => {
        return [...acc, ...faculty.questions];
    }, []);

    // Удаляем дубликаты из массива вопросов
    const uniqueQuestions = [...new Set(allQuestions.map(q => JSON.stringify(q)))].map(q => JSON.parse(q));

    selectRandomQuestion(uniqueQuestions, setQuestions);
    setStartNewQuiz(false);
};

const selectRandomQuestion = (questions, setQuestions) => {
    if (questions.length === 0) return;

    const randomIndex = Math.floor(Math.random() * questions.length);
    const newQuestion = questions[randomIndex];
    setQuestions(newQuestion);

    // Удаление выбранного вопроса из списка
    const updatedQuestions = questions.filter((_, index) => index !== randomIndex);
    localStorage.setItem('uniqueQuestions', JSON.stringify(updatedQuestions));
};

const checkQuestion = (question, numberQuestion, setProcent) => {
    // Получаем факультеты из localStorage
    let facultiesData = localStorage.getItem('faculties');
    if (!facultiesData) {
        console.error('Faculties data is not available in localStorage.');
        return;
    }
    facultiesData = JSON.parse(facultiesData);

    facultiesData.forEach((faculty) => {
        faculty.questions.forEach((q) => {
            if (q === question) {
                faculty.percent += Math.ceil((100 / faculty.questions.length) / 2 * numberQuestion);
            }
        });
    });

    // Обновляем данные факультетов в localStorage
    localStorage.setItem('faculties', JSON.stringify(facultiesData));
    findFavoriteDish(setProcent);
};


// Проверка на завершение
const examinationQuestion = (setResult, setIsResult) => {
    let facultiesData = localStorage.getItem('faculties');
    if (!facultiesData) {
        console.error('Faculties data is not available in localStorage.');
        return;
    }
    facultiesData = JSON.parse(facultiesData);

    for (const faculty of facultiesData) {
        if (faculty.percent >= PROCENT_MAX) {
            setIsResult(true)
            setResult(`Вам подходит кафедра: '${faculty.department}'.`);
        }
    }
};

// Новый вопрос
export const newQuestion = (setQuestions, numberQuestion, question, setProcent, setResult, result, setIsResult) => {
    const uniqueQuestions = localStorage.getItem('uniqueQuestions');
    if (uniqueQuestions) {
        const parsedQuestions = JSON.parse(uniqueQuestions);
        checkQuestion(question, numberQuestion, setProcent);
        examinationQuestion(setResult, setIsResult);
        selectRandomQuestion(parsedQuestions, setQuestions);
    }
};

// Прогресс бар
export const findFavoriteDish = (setProcent) => {
    let facultiesData = localStorage.getItem('faculties');
    if (!facultiesData) {
        console.error('Faculties data is not available in localStorage.');
        return;
    }
    facultiesData = JSON.parse(facultiesData);

    const favoriteDish = facultiesData.reduce((maxDish, currentDish) => {
        return currentDish.percent > maxDish.percent ? currentDish : maxDish;
    });

    console.log(favoriteDish.percent);
    setProcent(favoriteDish.percent);
};

// попробовать снова
export const newQuizFull = (setIsResult, setProcent, setQuestions, setStartNewQuiz) => {
    localStorage.setItem('faculties', JSON.stringify(faculties.faculties)); 
    setIsResult(false); 
    setProcent(0); 
    setQuestions(''); 
    setStartNewQuiz(true); 
};