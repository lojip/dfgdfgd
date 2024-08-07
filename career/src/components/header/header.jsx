import { Link } from 'react-router-dom';
import './header.scss';

const header = () => {
    return (
        <header className='header'>
            <img src="./logo.svg" alt="logo" />
            <nav>
                <ul>
                    <li><a href="#">Направления</a></li>
                    <li><a href="#">Результат</a></li>
                    <li>
                        <Link to="/">Главная</Link>
                    </li>
                </ul>
            </nav>
        </header>
    )
}

export default header