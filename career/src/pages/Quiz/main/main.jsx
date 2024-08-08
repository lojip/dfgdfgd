import style from './main.module.scss';
import { useEffect, useState } from 'react';
import { startQuiz, newQuestion, newQuizFull } from './quizUtils.jsx';

const Main = ({ newQuiz = true }) => {
    const [startNewQuiz, setStartNewQuiz] = useState(newQuiz);
    const [question, setQuestions] = useState('');
    const [procent, setProcent] = useState(0);
    const [isResult, setIsResult] = useState(false);
    const [result, setResult] = useState('');

    useEffect(() => {
        if (newQuiz) {
            setStartNewQuiz(true);
        }
    }, [newQuiz]);

    const data = [
        { number: 5, text: 'Очень подходит, сильно' },
        { number: 4, text: 'Подходит, нормально' },
        { number: 3, text: 'Средне(ние)' },
        { number: 2, text: 'Не подходит, чуть ниже среднего' },
        { number: 1, text: 'Вообще не подходит, плохо' },
    ];

    const handleNewQuestion = (itemNumber) => {
        newQuestion(setQuestions, itemNumber, question, setProcent, setResult, result, setIsResult, setStartNewQuiz);
    };

    return (
        <main className={style.main}>
            {isResult ? (
                <div className={style.containerQuiz}>
                    <div className={style.containerQuizWrapper}>
                        <h2 className={style.wrapperResultHeader}>Вам подойдет данная кафедра:</h2>
                    </div>
                    <div>
                        <h1 className={style.textResult}>
                            {result ? result : 'Вы еще не прошли тест'}
                        </h1>
                    </div>
                    <div className={style.containerButton}>
                        <a onClick={() => newQuizFull(setIsResult, setProcent, setQuestions, setStartNewQuiz)}>
                            Попробовать снова
                        </a>
                    </div>
                </div>
            ) : (
                startNewQuiz ? (
                    <div className={style.containerQuiz}>
                        <div className={style.wrapper}>
                            <h2>Какую стоить выбрать кафедру?</h2>
                        </div>
                        <div className={style.containerButton}>
                            <a onClick={() => startQuiz(setQuestions, setStartNewQuiz)}>
                                Узнать
                            </a>
                        </div>
                    </div>
                ) : (
                    <div className={style.containerQuiz}>
                        <div className={style.progress}>
                            <div style={{ width: `${procent}%`}} className={style.progress__inner}></div>
                        </div>
                        <div className={style.containerQuizWrapper}>
                            <h2 className={style.wrapperHeader}>{question}</h2>
                        </div>
                        <ul className={style.ul}>
                            {data.map((item, index) => (
                                <a key={index} onClick={() => handleNewQuestion(item.number)}>
                                    <li>
                                        {item.number} - {item.text}
                                    </li>
                                </a>
                            ))}
                        </ul>
                    </div>
                )
            )}
        </main>
    );
};

export default Main;