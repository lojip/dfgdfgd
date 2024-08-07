import { Link } from "react-router-dom";
import style from './main.module.scss';
import universite from '../../../../public/db_universities.json';

const Main = () => {
    return (
        <main className={style.main}>
            {universite.universitie.map((department, index) => (
                <section key={index}>
                    <div className={style.containerNewQuiz}>
                        <div className={style.logo}>
                            <img src="image.png" alt="logo university" />
                        </div>
                        <div className={style.wrapper}>
                            <div className={style.description}>
                                <h2>{department.name}</h2>
                                <p>{department.description}</p>
                            </div>
                            <div className={style.containerButton}>
                                <Link to='/quiz'>
                                    Пройти тест
                                </Link>
                            </div>
                        </div>
                    </div>
                </section>
            ))}
        </main>
    );
};

export default Main;