import './main.scss'

const main = () => {
    return (
        <main className='main'>
            <div className="containerQuiz">
                <div className="wrapper">
                    <h2>Choose your delivery option:</h2>
                </div>
                <div className="containerButton">                      
                    <ul>
                        <li>
                            <input type="radio" id="s-option" name="selector"></input>
                            <label for="s-option">1 -</label>
                            <div class="check"></div>
                        </li>
                        <li>
                            <input type="radio" id="d-option" name="selector"></input>
                            <label for="d-option">2 -</label>
                            <div class="check"><div class="inside"></div></div>
                        </li>
                        <li>
                            <input type="radio" id="o-option" name="selector"></input>
                            <label for="o-option">3 -</label>
                            <div class="check"><div class="inside"></div></div>
                        </li>
                        <li>
                            <input type="radio" id="o-option" name="selector"></input>
                            <label for="o-option">4 -</label>
                            <div class="check"><div class="inside"></div></div>
                        </li>
                        <li>
                            <input type="radio" id="o-option" name="selector"></input>
                            <label for="o-option">5 -</label>
                            <div class="check"><div class="inside"></div></div>
                        </li>
                    </ul>
                </div>
            </div>
        </main>
    )
}

export default main