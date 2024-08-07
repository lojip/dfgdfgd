import { Link } from 'react-router-dom';
import style from './main.module.scss';
import { useEffect, useState } from 'react';
import faculties from '../../../../public/db_faculties.json'

const Main = ({ newQuiz = true }) => {
    const [url, setUrl] = useState('/quiz');
    const [startNewQuiz, setStartNewQuiz] = useState(newQuiz); 

    const startQuiz = () => {
        console.log(faculties)
        setStartNewQuiz(false); 
    };

    useEffect(() => {
        setStartNewQuiz(newQuiz); 
    }, []);

    return (
        <main className={style.main}>
            {startNewQuiz ? (
                <div className={style.containerQuiz}>
                <div className={style.wrapper}>
                    {/* <h3>
                        Уверены, что вы выбрали именно ту кафедру? 
                    </h3> */}
                    <h2>Какую стоить выбрать кафедру?</h2>
                </div>
                <div className={style.containerButton}>
                    <a onClick={startQuiz}>
                        Узнать
                    </a>
                </div>
            </div>
            ) : (
                <div className={style.containerQuiz}>
                    <div className={style.progress}>
                        <div style={{ width: '75%' }} className={style.progress__inner}></div>
                    </div>
                    <div className={style.containerQuizwrapper}>
                        <h2>Тестоывый вариант вопроса</h2>
                    </div>
                    <ul className={style.ul}>
                        <li><Link to={url}>5 - Очень подходит</Link></li>
                        <li><Link to={url}>4 - Подходит</Link></li>
                        <li><Link to={url}>3 - Средне</Link></li>
                        <li><Link to={url}>2 - Не подходит</Link></li>
                        <li><Link to={url}>1 - Вообще не подходит</Link></li>
                    </ul>
                </div>
            )}
        </main>
    );
}

export default Main;