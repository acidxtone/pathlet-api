module.exports = {
    root: true,
    parser: '@typescript-eslint/parser',
    plugins: [
        '@typescript-eslint',
        'react'
    ],
    extends: [
        'eslint:recommended',
        'plugin:react/recommended',
        'plugin:@typescript-eslint/recommended',
        'react-app',
        'react-app/jest'
    ],
    rules: {
        'react/react-in-jsx-scope': 'off',
        'no-console': 'warn',
        '@typescript-eslint/explicit-module-boundary-types': 'off',
        'react/prop-types': 'off'
    },
    settings: {
        react: {
            version: 'detect'
        }
    }
};
