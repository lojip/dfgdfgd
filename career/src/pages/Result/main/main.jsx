import { Link } from 'react-router-dom'
import style from './main.module.scss'

const main = () => {
    return(
        <main className={style.main}>
        <div className={style.containerQuiz}>
            <div className={style.containerQuizwrapper}>
                <h2>Вам подойдет кафедра:</h2>
            </div>
            <div>
                <h4>Результат</h4>
            </div>
            <div className={style.containerButton}>
                    <Link to='/'>
                        Попробовать снова
                    </Link>
            </div>
        </div>
    </main>
    )
}

export default main