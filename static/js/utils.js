/**
 * Querying Elements With Tagged Template Literals
 */

export function queryAll(strings, ...values) {
    const string = values.reduce( (finalString, value, index) => {
        return `${finalString}${value}${strings[index + 1]}`
    }, strings[0])

    return document.querySelectorAll(string);
}

/**
 * Querying Single HTML Element With Tagged Template Literalss
 * @param strings
 * @param values
 */
export function query(strings, ...values) {
    const string = values.reduce( (finalString, value, index) => {
        return `${finalString}${value}${strings[index + 1]}`
    }, strings[0])

    return document.querySelector(string);
}

/**
 * Tagged template that returns bolded variables HTML text
 * @param strings
 * @param values
 * ex.     console.log(bold`xx ${x}`) // xx<strong>${x}</strong>
 */
export function bold(strings, ...values){
    return values.reduce( (acc, value, index) => {
        return `${acc}<strong>${value}</strong>${strings[index+1]}`
    }, strings[0]);
}

/**
 * Function that creates HTML element, assigns class
 * @param strings
 * @param classList
 * @param values
 */
export function create(strings, classList, ...values) {
    const element = document.createElement(strings[0]);
    if (classList instanceof Array)
       classList.forEach( (className) => element.classList.add(className) )
    else
        element.classList.add(classList)

   return element;
}


/**
 * USAGE:
 *      console.log(queryAll`div`)
 *      console.log(query`div`)
 *      console.log(create`div${'abc'}${'<h1> XX </h1>'}`)
 *      console.log(create`div${['abc', 'cde']}${'<h1> XX </h1>'}`)
 */