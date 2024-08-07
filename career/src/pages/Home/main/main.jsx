import { Link } from "react-router-dom";
import './main.scss'

const main = () => {
    return (
        <main className="main">
            <div className="containerQuiz">
                <div className="wrapper">
                    {/* <h3>
                        Уверены, что вы выбрали именно ту кафедру? 
                    </h3> */}
                    <h2>Какую стоить выбрать кафедру?</h2>
                </div>
                <div className="containerButton">
                    {/* <Link to='#'>
                        Проверить
                    </Link> */}
                    <Link to='/quiz'>
                        Узнать
                    </Link>
                </div>
            </div>
        </main>
    )
}

export default main;